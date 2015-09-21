from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'pywars.views.index', name='index'),
    url(r'^(?P<match_id>\d+)$', 'pywars.views.index', name='view_match'),
    url(r'^scoreboard$', 'pywars.views.scoreboard', name='scoreboard'),
    url(r'^tournament$', 'pywars.views.tournament', name='tournament'),
    url(r'^mybots$', 'pywars.views.mybots', name='mybots'),
    url(r'^about$', 'pywars.views.about', name='about'),
    url(r'^challenge$', 'pywars.views.challenge', name='challenge'),
    url(r'^main-match$', 'pywars.views.main_match', name='main_match'),
    url(r'^my-matches$', 'pywars.views.my_matches', name='my_matches'),
    url(r'^test-match$', 'pywars.views.random_test_match', name='test_match'),
    url(r'^get_match/(\d+)$', 'pywars.views.get_match', name='get_match'),
    url(r'^bot_code/(\d+)$', 'pywars.views.bot_code', name='bot_code'),
    url(r'^get_playlist$', 'pywars.views.get_playlist', name='get_playlist'),
    url(r'^get_bot_status/(\d+)$', 'pywars.views.get_bot_status', name='get_bot_status')
)
