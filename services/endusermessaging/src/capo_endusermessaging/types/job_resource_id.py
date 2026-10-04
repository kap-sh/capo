"""Generated from Smithy shape ``com.amazonaws.endusermessaging#JobResourceId``."""

from typing import TypeAlias

"""Identifier of a resource created or updated by a job (registration ID or brand profile ID). This is a distinct type from BrandProfileIdOrArn and RegistrationIdOrArn because: 1. It represents the *result* of a job, not an *input* identifier 2. Jobs can produce different resource types, so this is intentionally generic 3. Semantic clarity: callers see "JobResourceId" and understand it came from a job"""
JobResourceId: TypeAlias = str
