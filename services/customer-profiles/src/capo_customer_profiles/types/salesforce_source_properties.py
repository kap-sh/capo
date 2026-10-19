"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SalesforceSourceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.boolean
    import capo_customer_profiles.types.object


class SalesforceSourceProperties(TypedDict, closed=True):
    object: "capo_customer_profiles.types.object.Object"
    """<p>The object specified in the Salesforce flow source.</p>"""
    enable_dynamic_field_update: "capo_customer_profiles.types.boolean.boolean"
    """<p>The flag that enables dynamic fetching of new (recently added) fields in the Salesforce objects while running a flow.</p>"""
    include_deleted_records: "capo_customer_profiles.types.boolean.boolean"
    """<p>Indicates whether Amazon AppFlow includes deleted files in the flow run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SalesforceSourceProperties) -> dict:
    out: dict = {}
    out["Object"] = value["object"]
    out["EnableDynamicFieldUpdate"] = value.get("enable_dynamic_field_update", False)
    out["IncludeDeletedRecords"] = value.get("include_deleted_records", False)
    return out


def deserialize_json(data: dict) -> SalesforceSourceProperties:
    out: SalesforceSourceProperties = {}  # type: ignore[typeddict-item]
    if data.get("Object") is not None:
        out["object"] = data["Object"]
    else:
        out["object"] = ""
    if data.get("EnableDynamicFieldUpdate") is not None:
        out["enable_dynamic_field_update"] = data["EnableDynamicFieldUpdate"]
    else:
        out["enable_dynamic_field_update"] = False
    if data.get("IncludeDeletedRecords") is not None:
        out["include_deleted_records"] = data["IncludeDeletedRecords"]
    else:
        out["include_deleted_records"] = False
    return out
