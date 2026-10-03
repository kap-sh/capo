"""Generated from Smithy shape ``com.amazonaws.cloudformation#PublishTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.private_type_arn
    import capo_cloudformation.types.public_version_number
    import capo_cloudformation.types.third_party_type
    import capo_cloudformation.types.type_name


class PublishTypeInput(TypedDict, closed=True):
    type: NotRequired["capo_cloudformation.types.third_party_type.ThirdPartyType"]
    """<p>The type of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>"""
    arn: NotRequired["capo_cloudformation.types.private_type_arn.PrivateTypeArn"]
    """<p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>"""
    type_name: NotRequired["capo_cloudformation.types.type_name.TypeName"]
    """<p>The name of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>"""
    public_version_number: NotRequired[
        "capo_cloudformation.types.public_version_number.PublicVersionNumber"
    ]
    """<p>The version number to assign to this version of the extension.</p> <p>Use the following format, and adhere to semantic versioning when assigning a version number to your extension:</p> <p> <code>MAJOR.MINOR.PATCH</code> </p> <p>For more information, see <a href="https://semver.org/">Semantic Versioning 2.0.0</a>.</p> <p>If you don't specify a version number, CloudFormation increments the version number by one minor version release.</p> <p>You cannot specify a version number the first time you publish a type. CloudFormation automatically sets the first version number to be <code>1.0.0</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PublishTypeInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "type" in value:
        import capo_cloudformation.types.third_party_type

        capo_cloudformation.types.third_party_type.serialize_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "arn" in value:
        pairs.append((f"{key_prefix}Arn", str(value["arn"])))
    if "type_name" in value:
        pairs.append((f"{key_prefix}TypeName", str(value["type_name"])))
    if "public_version_number" in value:
        pairs.append(
            (f"{key_prefix}PublicVersionNumber", str(value["public_version_number"]))
        )


def deserialize_query(el: Element) -> PublishTypeInput:
    out: PublishTypeInput = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import capo_cloudformation.types.third_party_type

        out["type"] = capo_cloudformation.types.third_party_type.deserialize_query(
            child_type
        )
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_type_name = el.find("TypeName")
    if child_type_name is not None:
        out["type_name"] = str(child_type_name.text or "")
    child_public_version_number = el.find("PublicVersionNumber")
    if child_public_version_number is not None:
        out["public_version_number"] = str(child_public_version_number.text or "")
    return out
