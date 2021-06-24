from django.urls import path
from .views import (my_profile_view,
    invite_received_view, 
    profiles_list_view,
    invites_profiles_list_view,
    ProfileListView,
    ProfileDetailView,
    send_invitation,
    remove_form_friends,
    accept_invitation,
    reject_invitation,
)



app_name = 'profiles'

urlpatterns = [
    path("", ProfileListView.as_view(), name="all-profiles-veiw"),
    path("myprofile/",my_profile_view, name="my-profile-veiw"),
    path("myinvites/", invite_received_view, name="my-invites-veiw"),
    path("invite-profiles/", invites_profiles_list_view, name="invite-profiles-veiw"),
    path("send-invite/", send_invitation,name="send-invite-veiw"),
    path("remove-friend/", remove_form_friends, name="remove-friend"),
    path("<slug>/", ProfileDetailView.as_view(), name="profile-detail-veiw"),
    path("myinvites/accept/", accept_invitation, name="accept-invite"),
    path("myinvites/reject/", reject_invitation, name="reject-invite"),
]
