"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#SearchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudsearch_domain.types.cursor
    import capo_cloudsearch_domain.types.expr
    import capo_cloudsearch_domain.types.facet
    import capo_cloudsearch_domain.types.filter_query
    import capo_cloudsearch_domain.types.highlight
    import capo_cloudsearch_domain.types.partial
    import capo_cloudsearch_domain.types.query
    import capo_cloudsearch_domain.types.query_options
    import capo_cloudsearch_domain.types.query_parser
    import capo_cloudsearch_domain.types.return_
    import capo_cloudsearch_domain.types.size
    import capo_cloudsearch_domain.types.sort
    import capo_cloudsearch_domain.types.start
    import capo_cloudsearch_domain.types.stat

SearchRequest = TypedDict(
    "SearchRequest",
    {
        "cursor": NotRequired["capo_cloudsearch_domain.types.cursor.Cursor"],
        "expr": NotRequired["capo_cloudsearch_domain.types.expr.Expr"],
        "facet": NotRequired["capo_cloudsearch_domain.types.facet.Facet"],
        "filter_query": NotRequired[
            "capo_cloudsearch_domain.types.filter_query.FilterQuery"
        ],
        "highlight": NotRequired["capo_cloudsearch_domain.types.highlight.Highlight"],
        "partial": NotRequired["capo_cloudsearch_domain.types.partial.Partial"],
        "query": "capo_cloudsearch_domain.types.query.Query",
        "query_options": NotRequired[
            "capo_cloudsearch_domain.types.query_options.QueryOptions"
        ],
        "query_parser": NotRequired[
            "capo_cloudsearch_domain.types.query_parser.QueryParser"
        ],
        "return": NotRequired["capo_cloudsearch_domain.types.return_.Return"],
        "size": NotRequired["capo_cloudsearch_domain.types.size.Size"],
        "sort": NotRequired["capo_cloudsearch_domain.types.sort.Sort"],
        "start": NotRequired["capo_cloudsearch_domain.types.start.Start"],
        "stats": NotRequired["capo_cloudsearch_domain.types.stat.Stat"],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: SearchRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SearchRequest:
    out: SearchRequest = {}  # type: ignore[typeddict-item]
    return out
