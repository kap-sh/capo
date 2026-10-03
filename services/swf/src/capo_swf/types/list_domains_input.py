"""Generated from Smithy shape ``com.amazonaws.swf#ListDomainsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.page_size
    import capo_swf.types.page_token
    import capo_swf.types.registration_status
    import capo_swf.types.reverse_order


class ListDomainsInput(TypedDict, closed=True):
    next_page_token: NotRequired["capo_swf.types.page_token.PageToken"]
    """<p>If <code>NextPageToken</code> is returned there are more results available. The value of <code>NextPageToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return a <code>400</code> error: "<code>Specified token has exceeded its maximum lifetime</code>". </p> <p>The configured <code>maximumPageSize</code> determines how many results can be returned in a single call. </p>"""
    registration_status: "capo_swf.types.registration_status.RegistrationStatus"
    """<p>Specifies the registration status of the domains to list.</p>"""
    maximum_page_size: "capo_swf.types.page_size.PageSize"
    """<p>The maximum number of results that are returned per call. Use <code>nextPageToken</code> to obtain further pages of results. </p>"""
    reverse_order: "capo_swf.types.reverse_order.ReverseOrder"
    """<p>When set to <code>true</code>, returns the results in reverse order. By default, the results are returned in ascending alphabetical order by <code>name</code> of the domains.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDomainsInput) -> dict:
    out: dict = {}
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    import capo_swf.types.registration_status

    out["registrationStatus"] = (
        capo_swf.types.registration_status.serialize_aws_json_1_0(
            value["registration_status"]
        )
    )
    out["maximumPageSize"] = value.get("maximum_page_size", 0)
    out["reverseOrder"] = value.get("reverse_order", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDomainsInput:
    out: ListDomainsInput = {}  # type: ignore[typeddict-item]
    if data.get("nextPageToken") is not None:
        out["next_page_token"] = data["nextPageToken"]
    if data.get("registrationStatus") is not None:
        import capo_swf.types.registration_status

        out["registration_status"] = (
            capo_swf.types.registration_status.deserialize_aws_json_1_0(
                data["registrationStatus"]
            )
        )
    else:
        raise DeserializationError("ListDomainsInput.registration_status required")
    if data.get("maximumPageSize") is not None:
        out["maximum_page_size"] = data["maximumPageSize"]
    else:
        out["maximum_page_size"] = 0
    if data.get("reverseOrder") is not None:
        out["reverse_order"] = data["reverseOrder"]
    else:
        out["reverse_order"] = False
    return out
