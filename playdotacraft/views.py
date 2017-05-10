from django.views.generic import DetailView
from django.views.generic import ListView

from api.models import Match, Player, MatchPlayerResults


class MatchListView(ListView):

    model = Match
    template_name = 'match_list.html'

    def get_context_data(self, **kwargs):
        context = super(MatchListView, self).get_context_data(**kwargs)
        return context

    def get_template_names(self):
        return self.template_name


class PlayerListView(ListView):

    model = Player
    template_name = 'player_list.html'

    def get_context_data(self, **kwargs):
        context = super(PlayerListView, self).get_context_data(**kwargs)
        return context

    def get_template_names(self):
        return self.template_name


class MatchDetailView(DetailView):

    model = Match
    template_name = 'match_details.html'

    def get_context_data(self, **kwargs):
        context = super(MatchDetailView, self).get_context_data(**kwargs)
        context['results'] = MatchPlayerResults.objects.filter(match=self.object)
        return context
