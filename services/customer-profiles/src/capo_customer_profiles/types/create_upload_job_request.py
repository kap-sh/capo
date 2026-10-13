"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateUploadJobRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.expiration_days_integer
    import capo_customer_profiles.types.field_map
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.text


class CreateUploadJobRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain. Domain should be exists for the upload job to be created. </p>"""
    display_name: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>The unique name of the upload job. Could be a file name to identify the upload job.</p>"""
    fields: "capo_customer_profiles.types.field_map.FieldMap"
    """<p>The mapping between CSV Columns and Profile Object attributes. A map of the name and ObjectType field.</p>"""
    unique_key: "capo_customer_profiles.types.text.text"
    """<p>The unique key columns for de-duping the profiles used to map data to the profile. </p>"""
    data_expiry: NotRequired[
        "capo_customer_profiles.types.expiration_days_integer.expirationDaysInteger"
    ]
    """<p>The expiry duration for the profiles ingested with the job. If not provided, the system default of 2 weeks is used. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUploadJobRequest) -> dict:
    out: dict = {}
    out["DisplayName"] = value["display_name"]
    import capo_customer_profiles.types.field_map

    out["Fields"] = capo_customer_profiles.types.field_map.serialize_json(
        value["fields"]
    )
    out["UniqueKey"] = value["unique_key"]
    if "data_expiry" in value:
        out["DataExpiry"] = value["data_expiry"]
    return out


def deserialize_json(data: dict) -> CreateUploadJobRequest:
    out: CreateUploadJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    else:
        raise DeserializationError("CreateUploadJobRequest.display_name required")
    if data.get("Fields") is not None:
        import capo_customer_profiles.types.field_map

        out["fields"] = capo_customer_profiles.types.field_map.deserialize_json(
            data["Fields"]
        )
    else:
        raise DeserializationError("CreateUploadJobRequest.fields required")
    if data.get("UniqueKey") is not None:
        out["unique_key"] = data["UniqueKey"]
    else:
        raise DeserializationError("CreateUploadJobRequest.unique_key required")
    if data.get("DataExpiry") is not None:
        out["data_expiry"] = data["DataExpiry"]
    return out


def redact_sensitive(value: CreateUploadJobRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "fields" in value:
        out["fields"] = "*** Sensitive Data Redacted ***"
    return out
