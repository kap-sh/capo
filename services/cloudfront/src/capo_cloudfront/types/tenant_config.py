"""Generated from Smithy shape ``com.amazonaws.cloudfront#TenantConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.parameter_definitions


class TenantConfig(TypedDict, closed=True):
    parameter_definitions: NotRequired[
        "capo_cloudfront.types.parameter_definitions.ParameterDefinitions"
    ]
    """<p>The parameters that you specify for a distribution tenant.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: TenantConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "parameter_definitions" in value:
        import capo_cloudfront.types.parameter_definitions

        capo_cloudfront.types.parameter_definitions.serialize_xml(
            value["parameter_definitions"], el, "ParameterDefinitions"
        )


def deserialize_xml(el: Element) -> TenantConfig:
    out: TenantConfig = {}  # type: ignore[typeddict-item]
    child_parameter_definitions = el.find("ParameterDefinitions")
    if child_parameter_definitions is not None:
        import capo_cloudfront.types.parameter_definitions

        out["parameter_definitions"] = (
            capo_cloudfront.types.parameter_definitions.deserialize_xml(
                child_parameter_definitions
            )
        )
    return out


def redact_sensitive(value: TenantConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "parameter_definitions" in value:
        import capo_cloudfront.types.parameter_definitions

        out["parameter_definitions"] = (
            capo_cloudfront.types.parameter_definitions.redact_sensitive(
                value["parameter_definitions"]
            )
        )
    return out
