"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetIdentifierDeclaration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.data_set_identifier


class DataSetIdentifierDeclaration(TypedDict, closed=True):
    identifier: "capo_quicksight.types.data_set_identifier.DataSetIdentifier"
    """<p>The identifier of the data set, typically the data set's name.</p>"""
    data_set_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the data set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetIdentifierDeclaration) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    out["DataSetArn"] = value["data_set_arn"]
    return out


def deserialize_json(data: dict) -> DataSetIdentifierDeclaration:
    out: DataSetIdentifierDeclaration = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("DataSetArn") is not None:
        out["data_set_arn"] = data["DataSetArn"]
    else:
        out["data_set_arn"] = ""
    return out
