"""Generated from Smithy shape ``com.amazonaws.appstream#EmbedHostDomain``."""

from typing import TypeAlias

"""Specifies a valid domain that can embed AppStream. Valid examples include: ["testorigin.tt--com", "testingorigin.com.us", "test.com.us"] Invalid examples include: ["test,com", ".com", "h*llo.com". ""]"""
EmbedHostDomain: TypeAlias = str
