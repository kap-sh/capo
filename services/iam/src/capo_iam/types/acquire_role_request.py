"""Generated from Smithy shape ``com.amazonaws.iam#AcquireRoleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.integer_type
    import capo_iam.types.map_string_replacement_value_entry


class AcquireRoleRequest(TypedDict, closed=True):
    template_arn: "capo_iam.types.arn_type.arnType"
    """<p>The Amazon Resource Name (ARN) of the role template to create the role from.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    template_minor_version: NotRequired["capo_iam.types.integer_type.integerType"]
    """<p>The minor version of the role template to use. If you do not specify a minor version, the service uses the template's default minor version.</p>"""
    replacement_values: NotRequired[
        "capo_iam.types.map_string_replacement_value_entry.mapStringReplacementValueEntry"
    ]
    """<p>A map of values to substitute for the parameters that are defined in the role template version. Each key is a parameter name from the template, and each value is a structure that contains the replacement values for that parameter.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AcquireRoleRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}TemplateArn", str(value["template_arn"])))
    if "template_minor_version" in value:
        pairs.append(
            (f"{key_prefix}TemplateMinorVersion", str(value["template_minor_version"]))
        )
    if "replacement_values" in value:
        import capo_iam.types.map_string_replacement_value_entry

        capo_iam.types.map_string_replacement_value_entry.serialize_query(
            value["replacement_values"], pairs, f"{key_prefix}ReplacementValues"
        )


def deserialize_query(el: Element) -> AcquireRoleRequest:
    out: AcquireRoleRequest = {}  # type: ignore[typeddict-item]
    child_template_arn = el.find("TemplateArn")
    if child_template_arn is not None:
        out["template_arn"] = str(child_template_arn.text or "")
    else:
        raise DeserializationError("AcquireRoleRequest.template_arn required")
    child_template_minor_version = el.find("TemplateMinorVersion")
    if child_template_minor_version is not None:
        out["template_minor_version"] = int(child_template_minor_version.text or "")
    child_replacement_values = el.find("ReplacementValues")
    if child_replacement_values is not None:
        import capo_iam.types.map_string_replacement_value_entry

        out["replacement_values"] = (
            capo_iam.types.map_string_replacement_value_entry.deserialize_query(
                child_replacement_values
            )
        )
    return out
