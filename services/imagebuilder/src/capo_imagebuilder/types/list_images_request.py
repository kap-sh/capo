"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListImagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.boolean
    import capo_imagebuilder.types.filter_list
    import capo_imagebuilder.types.nullable_boolean
    import capo_imagebuilder.types.ownership
    import capo_imagebuilder.types.pagination_token
    import capo_imagebuilder.types.restricted_integer


class ListImagesRequest(TypedDict, closed=True):
    owner: NotRequired["capo_imagebuilder.types.ownership.Ownership"]
    """<p>Filters the list to images owned by you, by Amazon, or shared with you by other accounts. By default, only your account's images are returned.</p>"""
    filters: NotRequired["capo_imagebuilder.types.filter_list.FilterList"]
    """<p>Use the following filters to streamline results:</p> <ul> <li> <p> <code>name</code> </p> </li> <li> <p> <code>osVersion</code> </p> </li> <li> <p> <code>platform</code> </p> </li> <li> <p> <code>type</code> </p> </li> <li> <p> <code>version</code> </p> </li> </ul>"""
    by_name: NotRequired["capo_imagebuilder.types.boolean.Boolean"]
    """<p>Specifies whether to return one entry per image name, with all versions of each image aggregated. Defaults to <code>false</code>, which returns one entry per image version. You can't combine this option with the <code>version</code> filter.</p>"""
    max_results: NotRequired[
        "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
    ]
    """<p>The maximum number of items to return in a single request.</p>"""
    next_token: NotRequired["capo_imagebuilder.types.pagination_token.PaginationToken"]
    """<p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>"""
    include_deprecated: NotRequired[
        "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether to include deprecated Amazon-managed images in the results. Deprecated images that you own are always returned. Defaults to <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImagesRequest) -> dict:
    out: dict = {}
    if "owner" in value:
        import capo_imagebuilder.types.ownership

        out["owner"] = capo_imagebuilder.types.ownership.serialize_json(value["owner"])
    if "filters" in value:
        import capo_imagebuilder.types.filter_list

        out["filters"] = capo_imagebuilder.types.filter_list.serialize_json(
            value["filters"]
        )
    if "by_name" in value:
        out["byName"] = value["by_name"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "include_deprecated" in value:
        out["includeDeprecated"] = value["include_deprecated"]
    return out


def deserialize_json(data: dict) -> ListImagesRequest:
    out: ListImagesRequest = {}  # type: ignore[typeddict-item]
    if data.get("owner") is not None:
        import capo_imagebuilder.types.ownership

        out["owner"] = capo_imagebuilder.types.ownership.deserialize_json(data["owner"])
    if data.get("filters") is not None:
        import capo_imagebuilder.types.filter_list

        out["filters"] = capo_imagebuilder.types.filter_list.deserialize_json(
            data["filters"]
        )
    if data.get("byName") is not None:
        out["by_name"] = data["byName"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("includeDeprecated") is not None:
        out["include_deprecated"] = data["includeDeprecated"]
    return out
