"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListManagedThingsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.managed_thing_list_definition
    import capo_iot_managed_integrations.types.next_token


class ListManagedThingsResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_iot_managed_integrations.types.managed_thing_list_definition.ManagedThingListDefinition"
    ]
    """<p>The list of managed things.</p>"""
    next_token: NotRequired["capo_iot_managed_integrations.types.next_token.NextToken"]
    """<p>A token that can be used to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedThingsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_iot_managed_integrations.types.managed_thing_list_definition

        out["Items"] = (
            capo_iot_managed_integrations.types.managed_thing_list_definition.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListManagedThingsResponse:
    out: ListManagedThingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_iot_managed_integrations.types.managed_thing_list_definition

        out["items"] = (
            capo_iot_managed_integrations.types.managed_thing_list_definition.deserialize_json(
                data["Items"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListManagedThingsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_iot_managed_integrations.types.managed_thing_list_definition

        out["items"] = (
            capo_iot_managed_integrations.types.managed_thing_list_definition.redact_sensitive(
                value["items"]
            )
        )
    return out
