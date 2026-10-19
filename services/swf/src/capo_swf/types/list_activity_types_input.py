"""Generated from Smithy shape ``com.amazonaws.swf#ListActivityTypesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.domain_name
    import capo_swf.types.name
    import capo_swf.types.page_size
    import capo_swf.types.page_token
    import capo_swf.types.registration_status
    import capo_swf.types.reverse_order


class ListActivityTypesInput(TypedDict, closed=True):
    domain: "capo_swf.types.domain_name.DomainName"
    """<p>The name of the domain in which the activity types have been registered.</p>"""
    name: NotRequired["capo_swf.types.name.Name"]
    """<p>If specified, only lists the activity types that have this name.</p>"""
    registration_status: "capo_swf.types.registration_status.RegistrationStatus"
    """<p>Specifies the registration status of the activity types to list.</p>"""
    next_page_token: NotRequired["capo_swf.types.page_token.PageToken"]
    """<p>If <code>NextPageToken</code> is returned there are more results available. The value of <code>NextPageToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return a <code>400</code> error: "<code>Specified token has exceeded its maximum lifetime</code>". </p> <p>The configured <code>maximumPageSize</code> determines how many results can be returned in a single call. </p>"""
    maximum_page_size: NotRequired["capo_swf.types.page_size.PageSize"]
    """<p>The maximum number of results that are returned per call. Use <code>nextPageToken</code> to obtain further pages of results. </p>"""
    reverse_order: NotRequired["capo_swf.types.reverse_order.ReverseOrder"]
    """<p>When set to <code>true</code>, returns the results in reverse order. By default, the results are returned in ascending alphabetical order by <code>name</code> of the activity types.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListActivityTypesInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    if "name" in value:
        out["name"] = value["name"]
    import capo_swf.types.registration_status

    out["registrationStatus"] = (
        capo_swf.types.registration_status.serialize_aws_json_1_0(
            value["registration_status"]
        )
    )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    if "maximum_page_size" in value:
        out["maximumPageSize"] = value["maximum_page_size"]
    if "reverse_order" in value:
        out["reverseOrder"] = value["reverse_order"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListActivityTypesInput:
    out: ListActivityTypesInput = {}  # type: ignore[typeddict-item]
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    else:
        out["domain"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("registrationStatus") is not None:
        import capo_swf.types.registration_status

        out["registration_status"] = (
            capo_swf.types.registration_status.deserialize_aws_json_1_0(
                data["registrationStatus"]
            )
        )
    else:
        import typing

        out["registration_status"] = typing.cast(
            "capo_swf.types.registration_status.RegistrationStatus", ""
        )
    if data.get("nextPageToken") is not None:
        out["next_page_token"] = data["nextPageToken"]
    if data.get("maximumPageSize") is not None:
        out["maximum_page_size"] = data["maximumPageSize"]
    if data.get("reverseOrder") is not None:
        out["reverse_order"] = data["reverseOrder"]
    return out
