"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#TemplateFieldId``."""

from typing import TypeAlias

"""A field's slot name — the developer-readable key that matches a {{fieldId}} placeholder in the layout skeleton (e.g. "Headline", "CtaUrl"), or the form field name in a document template (e.g. "Page 2 Title"). Platform-assigned and semantic (not a service-generated opaque Id), so it has its own constrained shape rather than reusing Id. Single spaces between words are allowed because document templates name their fields that way, and this shape is the input type for editing them. Leading, trailing and repeated spaces are not, so that "Title" and "Title " cannot be two different fields."""
TemplateFieldId: TypeAlias = str
