"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListAccountIntegrationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.max_size100
    import capo_customer_profiles.types.optional_boolean
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.token


class ListAccountIntegrationsRequest(TypedDict, closed=True):
    uri: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>The URI of the S3 bucket or any other type of data source.</p>"""
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous ListAccountIntegrations API call.</p>"""
    max_results: NotRequired["capo_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of objects returned per page.</p>"""
    include_hidden: NotRequired[
        "capo_customer_profiles.types.optional_boolean.optionalBoolean"
    ]
    """<p>Boolean to indicate if hidden integration should be returned. Defaults to <code>False</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccountIntegrationsRequest) -> dict:
    out: dict = {}
    out["Uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> ListAccountIntegrationsRequest:
    out: ListAccountIntegrationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Uri") is not None:
        out["uri"] = data["Uri"]
    else:
        out["uri"] = ""
    return out
