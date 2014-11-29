from django import forms

class TinyMCETextArea(forms.Textarea):
	class Media:
		js = ('static/tiny_mce/tinymce.min.js')