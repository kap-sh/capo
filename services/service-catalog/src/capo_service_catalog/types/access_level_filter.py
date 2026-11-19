"""Generated from Smithy shape ``com.amazonaws.servicecatalog#AccessLevelFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.access_level_filter_key
    import capo_service_catalog.types.access_level_filter_value


class AccessLevelFilter(TypedDict, closed=True):
    key: NotRequired[
        "capo_service_catalog.types.access_level_filter_key.AccessLevelFilterKey"
    ]
    """<p>The access level.</p> <ul> <li> <p> <code>Account</code> - Filter results based on the account.</p> </li> <li> <p> <code>Role</code> - Filter results based on the federated role of the specified user.</p> </li> <li> <p> <code>User</code> - Filter results based on the specified user.</p> </li> </ul>"""
    value: NotRequired[
        "capo_service_catalog.types.access_level_filter_value.AccessLevelFilterValue"
    ]
    """<p>The user to which the access level applies. The only supported value is <code>self</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessLevelFilter) -> dict:
    out: dict = {}
    if "key" in value:
        import capo_service_catalog.types.access_level_filter_key

        out["Key"] = (
            capo_service_catalog.types.access_level_filter_key.serialize_aws_json_1_1(
                value["key"]
            )
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessLevelFilter:
    out: AccessLevelFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        import capo_service_catalog.types.access_level_filter_key

        out["key"] = (
            capo_service_catalog.types.access_level_filter_key.deserialize_aws_json_1_1(
                data["Key"]
            )
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessLevelFilter) -> dict:
    out: dict = {}
    if "key" in value:
        import capo_service_catalog.types.access_level_filter_key

        out["Key"] = capo_service_catalog.types.access_level_filter_key.serialize_cbor(
            value["key"]
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_cbor(data: dict) -> AccessLevelFilter:
    out: AccessLevelFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        import capo_service_catalog.types.access_level_filter_key

        out["key"] = (
            capo_service_catalog.types.access_level_filter_key.deserialize_cbor(
                data["Key"]
            )
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
