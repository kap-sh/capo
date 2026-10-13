"""Generated from Smithy shape ``com.amazonaws.glue#TestConnectionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.test_connection_input


class TestConnectionRequest(TypedDict, closed=True):
    connection_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>Optional. The name of the connection to test. If only name is provided, the operation will get the connection and use that for testing.</p>"""
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The catalog ID where the connection resides.</p>"""
    test_connection_input: NotRequired[
        "capo_glue.types.test_connection_input.TestConnectionInput"
    ]
    """<p>A structure that is used to specify testing a connection to a service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestConnectionRequest) -> dict:
    out: dict = {}
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "test_connection_input" in value:
        import capo_glue.types.test_connection_input

        out["TestConnectionInput"] = (
            capo_glue.types.test_connection_input.serialize_aws_json_1_1(
                value["test_connection_input"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TestConnectionRequest:
    out: TestConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionName") is not None:
        out["connection_name"] = data["ConnectionName"]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("TestConnectionInput") is not None:
        import capo_glue.types.test_connection_input

        out["test_connection_input"] = (
            capo_glue.types.test_connection_input.deserialize_aws_json_1_1(
                data["TestConnectionInput"]
            )
        )
    return out


def redact_sensitive(value: TestConnectionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "test_connection_input" in value:
        import capo_glue.types.test_connection_input

        out["test_connection_input"] = (
            capo_glue.types.test_connection_input.redact_sensitive(
                value["test_connection_input"]
            )
        )
    return out
