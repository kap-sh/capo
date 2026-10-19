"""Generated from Smithy shape ``com.amazonaws.firehose#TableCreationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.boolean_object


class TableCreationConfiguration(TypedDict, closed=True):
    enabled: "capo_firehose.types.boolean_object.BooleanObject"
    """<p> Specify whether you want to enable automatic table creation. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableCreationConfiguration) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TableCreationConfiguration:
    out: TableCreationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out
