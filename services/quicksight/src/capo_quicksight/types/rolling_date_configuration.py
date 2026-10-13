"""Generated from Smithy shape ``com.amazonaws.quicksight#RollingDateConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_identifier
    import capo_quicksight.types.expression


class RollingDateConfiguration(TypedDict, closed=True):
    data_set_identifier: NotRequired[
        "capo_quicksight.types.data_set_identifier.DataSetIdentifier"
    ]
    """<p>The data set that is used in the rolling date configuration.</p>"""
    expression: "capo_quicksight.types.expression.Expression"
    """<p>The expression of the rolling date configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RollingDateConfiguration) -> dict:
    out: dict = {}
    if "data_set_identifier" in value:
        out["DataSetIdentifier"] = value["data_set_identifier"]
    out["Expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> RollingDateConfiguration:
    out: RollingDateConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("DataSetIdentifier") is not None:
        out["data_set_identifier"] = data["DataSetIdentifier"]
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    else:
        raise DeserializationError("RollingDateConfiguration.expression required")
    return out


def redact_sensitive(value: RollingDateConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    return out
