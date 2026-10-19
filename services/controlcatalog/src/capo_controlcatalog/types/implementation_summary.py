"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ImplementationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controlcatalog.types.implementation_identifier
    import capo_controlcatalog.types.implementation_type


class ImplementationSummary(TypedDict, closed=True):
    type: "capo_controlcatalog.types.implementation_type.ImplementationType"
    """<p>A string that represents the Amazon Web Services service that implements this control. For example, a value of <code>AWS::Config::ConfigRule</code> indicates that the control is implemented by Amazon Web Services Config, and <code>AWS::SecurityHub::SecurityControl</code> indicates implementation by Amazon Web Services Security Hub.</p>"""
    identifier: NotRequired[
        "capo_controlcatalog.types.implementation_identifier.ImplementationIdentifier"
    ]
    """<p>The identifier originally assigned by the Amazon Web Services service that implements the control. For example, <code>CODEPIPELINE_DEPLOYMENT_COUNT_CHECK</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImplementationSummary) -> dict:
    out: dict = {}
    out["Type"] = value["type"]
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> ImplementationSummary:
    out: ImplementationSummary = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        out["type"] = ""
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    return out
