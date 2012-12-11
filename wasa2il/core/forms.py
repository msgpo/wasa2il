from django.forms import ModelForm
from core.models import Topic, Issue, Comment, Document, Polity, Meeting

class TopicForm(ModelForm):
	class Meta:
		model = Topic
		exclude = ('polity', 'slug')


class IssueForm(ModelForm):
	class Meta:
		model = Issue
		exclude = ('slug', 'options')


class CommentForm(ModelForm):
	class Meta:
		model = Comment
		exclude = ('issue')


class DocumentForm(ModelForm):
	class Meta:
		model = Document
		exclude = ('is_adopted', 'is_proposed', 'user', 'polity', 'slug', 'issues')

class PolityForm(ModelForm):
	class Meta:
		model = Polity
		exclude = ('slug', 'parent', 'members', 'image')


class MeetingForm(ModelForm):
	class Meta:
		model = Meeting
		exclude = ('user', 'polity', 'is_agenda_open', 'managers', 'attendees', 'time_started', 'time_ended')
