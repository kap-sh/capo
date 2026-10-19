"""Generated from Smithy shape ``com.amazonaws.inspector2#ListConnectorScanConfigurationsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.connector_next_token
    import capo_inspector2.types.connector_scan_configuration_item_list


class ListConnectorScanConfigurationsResponse(TypedDict, closed=True):
    scan_configurations: "capo_inspector2.types.connector_scan_configuration_item_list.ConnectorScanConfigurationItemList"
    """<p>A list of scan configuration items.</p>"""
    next_token: NotRequired[
        "capo_inspector2.types.connector_next_token.ConnectorNextToken"
    ]
    """<p>A pagination token. If this value is not null, there are additional results available. Use this token in the <code>nextToken</code> parameter of a subsequent request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorScanConfigurationsResponse) -> dict:
    out: dict = {}
    import capo_inspector2.types.connector_scan_configuration_item_list

    out["scanConfigurations"] = (
        capo_inspector2.types.connector_scan_configuration_item_list.serialize_json(
            value["scan_configurations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConnectorScanConfigurationsResponse:
    out: ListConnectorScanConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("scanConfigurations") is not None:
        import capo_inspector2.types.connector_scan_configuration_item_list

        out["scan_configurations"] = (
            capo_inspector2.types.connector_scan_configuration_item_list.deserialize_json(
                data["scanConfigurations"]
            )
        )
    else:
        out["scan_configurations"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListConnectorScanConfigurationsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
