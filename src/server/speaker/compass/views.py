import os
from copy import deepcopy

from django.views.generic import DetailView, TemplateView, ListView, CreateView, View
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import CompassPage

from .questionnaire import q


class LeafDetail(DetailView):
    template_name = 'compass/leaf.html'


class CompassStartView(TemplateView):
    template_name = 'compass/start.html'


class CompassPageList(ListView):

    model = CompassPage
    template_name = 'compass/admin/list.html'


class CompassAddPage(CreateView):
    model = CompassPage
    template_name = 'compass/admin/add.html'


class QuestionnaireBaseView(TemplateView):

    def post(self, request, *args, **kwargs):
        dd = request.session.get('questionnaire', {})
        dd.update({self.step: request.POST.get('answer')})
        request.session['questionnaire'] = dd
        return HttpResponseRedirect(
            reverse('questionnaire_step', kwargs={'step': self.step + 1})
        )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'question': self.question,
            'answers': self.answers
        })
        return ctx

    @property
    def step(self):
        return int(self.kwargs.get('step', 0))

    @property
    def question(self):
        return q[self.step]['question']

    @property
    def answers(self):
        return q[self.step]['answers']

    def get(self, request, *args, **kwargs):
        try:
            q[self.step]
        except IndexError:
            return HttpResponseRedirect(reverse('questionnaire_completed'))
        return super().get(request, *args, **kwargs)


class QuestionnairePage(QuestionnaireBaseView):

    def get_template_names(self):
        base_template_dir = 'compass/questionnaire/'
        return [
            os.path.join(base_template_dir, '%d.html' % self.step),
            os.path.join(base_template_dir, 'base.html')
        ]


class QuestionnaireCompleted(TemplateView):
    template_name = 'compass/questionnaire/completed.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        qc = deepcopy(q)
        given_answers = self.request.session.get('questionnaire')

        for step, qa in enumerate(qc):
            a = given_answers.get(str(step))
            if a:
                answers = qa['answers']
                qa.update({'given_answer': answers[int(a)]})

        ctx.update({
            'questionnaire': qc,
            'answers': self.request.session.get('questionnaire')
        })
        return ctx
