"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeConnectorResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.described_connector


class DescribeConnectorResponse(TypedDict, closed=True):
    connector: "capo_transfer.types.described_connector.DescribedConnector"
    """<p>The structure that contains the details of the connector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConnectorResponse) -> dict:
    out: dict = {}
    import capo_transfer.types.described_connector

    out["Connector"] = capo_transfer.types.described_connector.serialize_aws_json_1_1(
        value["connector"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConnectorResponse:
    out: DescribeConnectorResponse = {}  # type: ignore[typeddict-item]
    if data.get("Connector") is not None:
        import capo_transfer.types.described_connector

        out["connector"] = (
            capo_transfer.types.described_connector.deserialize_aws_json_1_1(
                data["Connector"]
            )
        )
    else:
        raise DeserializationError("DescribeConnectorResponse.connector required")
    return out


def redact_sensitive(value: DescribeConnectorResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connector" in value:
        import capo_transfer.types.described_connector

        out["connector"] = capo_transfer.types.described_connector.redact_sensitive(
            value["connector"]
        )
    return out
