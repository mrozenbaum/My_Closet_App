from django.test import TestCase
from django.utils import timezone
import datetime
from django.urls import reverse



from .models import Owner


# Create your tests here.


class OwnerModelTests(TestCase):

    def test_was_published_recently_with_future_owner(self):
        '''
        was_published_recently() returns False for Owners whose pub_date
        is in the future
        '''
        time = timezone.now() + datetime.timedelta(days=30)
        future_owner = Owner(pub_date=time)
        self.assertIs(future_owner.was_published_recently(), False)


    def test_was_published_recently_with_old_owner(self):
        '''
        was_published_recently() returns False for Owners whose pub_date
        is older than 1 day
        '''
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_owner = Owner(pub_date=time)
        self.assertIs(old_owner.was_published_recently(), False)

    def test_was_published_recently_with_recent_owner(self):
        '''
        was_published_recently() returns True for Owners whose pub_date
        is within the last day
        '''
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_owner = Owner(pub_date=time)
        self.assertIs(recent_owner.was_published_recently(), True)




def create_owner(owner_name, days):
    '''
    create an Owner with the given `owner_name` and published the
    given number of `days` offset to now (negative for Owners published
    in the past, positive for Owners that have yet to be published).
    '''
    time = timezone.now() + datetime.timedelta(days=days)
    return Owner.objects.create(owner_name=owner_name, pub_date=time)



class OwnerIndexViewTests(TestCase):
    def test_no_owners(self):
        '''
        if no owners exist, an appropriate message is displayed.
        '''
        response = self.client.get(reverse('mycloset:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No closet's are available.")
        self.assertQuerysetEqual(response.context['latest_owner_list'], [])


    def test_past_owner(self):
        '''
        Owners with a pub_date in the past are displayed on the
        index page.
        '''
        create_owner(owner_name="Past Owner.", days=-30)
        response = self.client.get(reverse('mycloset:index'))
        self.assertQuerysetEqual(
            response.context['latest_owner_list'],
            ['<Owner: Past owner.>']
        )


    def test_future_owner(self):
        '''
        Owners with a pub_date in the future aren't displayed on
        the index page.
        '''
        create_owner(owner_name="Future Owner.", days=30)
        response = self.client.get(reverse('mycloset:index'))
        self.assertContains(response, "No Closet's are available.")
        self.assertQuerysetEqual(response.context['latest_owner_list'], [])


    def test_future_owner_and_past_owner(self):
        '''
        even if both past and future Owners exist, only past Owners
        are displayed.
        '''
        create_owner(owner_name="Past Owner.", days=-30)
        create_owner(owner_name="Future Owner.", days=30)
        response = self.client.get(reverse('mycloset:index'))
        self.assertQuerysetEqual(
            response.context['latest_owner_list'],
            ['<Owner: Past Owner.>']
        )


    def test_two_past_owners(self):
        '''
        the Owners index page may display multiple Owners.
        '''
        create_owner(owner_name="Past Owner 1.", days=-30)
        create_owner(owner_name="Past Owner 2.", days=-5)
        response = self.client.get(reverse('mycloset:index'))
        self.assertQuerysetEqual(
            response.context['latest_owner_list'],
            ['<Owner: Past Owner 2.>', '<Owner: Past Owner 1.>']
        )



class OwnerDetailViewTests(TestCase):
    def test_future_owner(self):
        '''
        the detail view of an Owner with a pub_date in the future
        returns a 404 not found.
        '''
        future_owner = create_owner(owner_name='Future Owner.', days=5)
        url = reverse('mycloset:detail', args=(future_owner.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


    def test_past_question(self):
        '''
        the detail view of an Owner with a pub_date in the past
        displays the Owner's name.
        '''
        past_owner = create_owner(owner_name='Past Owner.', days=-5)
        url = reverse('mycloset:detail', args=(past_owner.id,))
        response = self.client.get(url)
        self.assertContains(response, past_owner.owner_name)         
            




