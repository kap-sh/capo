"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#SearchSort``."""

from typing import TypeAlias

"""<p>A sort clause in OpenSearch Query DSL (the value of an OpenSearch <code>sort</code>): a field name, <code>{"field": "asc"|"desc"}</code>, <code>{"field": {"order": "asc"|"desc"}}</code>, or an array of these. Sorting is supported on <code>_score</code>, <code>system_metadata.created_at</code>, and <code>system_metadata.updated_at</code>.</p>"""
SearchSort: TypeAlias = object
