"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#FileReference``."""

from typing import TypeAlias

"""Opaque reference to an uploaded file. Sized for the read form as well as the write form: an image field's value comes back as a presigned URL, and one signed with session credentials is ~1,400 characters."""
FileReference: TypeAlias = str
