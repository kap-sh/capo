"""Generated from Smithy shape ``com.amazonaws.cloudformation#RequiredActivatedType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.publisher_id
    import capo_cloudformation.types.supported_major_versions
    import capo_cloudformation.types.type_name


class RequiredActivatedType(TypedDict, closed=True):
    type_name_alias: NotRequired["capo_cloudformation.types.type_name.TypeName"]
    """<p>An alias assigned to the public extension, in this account and Region. If you specify an alias for the extension, CloudFormation treats the alias as the extension type name within this account and Region. You must use the alias to refer to the extension in your templates, API calls, and CloudFormation console.</p>"""
    original_type_name: NotRequired["capo_cloudformation.types.type_name.TypeName"]
    """<p>The type name of the public extension.</p> <p>If you specified a <code>TypeNameAlias</code> when enabling the extension in this account and Region, CloudFormation treats that alias as the extension's type name within the account and Region, not the type name of the public extension. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-alias">Use aliases to refer to extensions</a> in the <i>CloudFormation User Guide</i>.</p>"""
    publisher_id: NotRequired["capo_cloudformation.types.publisher_id.PublisherId"]
    """<p>The publisher ID of the extension publisher.</p>"""
    supported_major_versions: NotRequired[
        "capo_cloudformation.types.supported_major_versions.SupportedMajorVersions"
    ]
    """<p>A list of the major versions of the extension type that the macro supports.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RequiredActivatedType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "type_name_alias" in value:
        pairs.append((f"{key_prefix}TypeNameAlias", str(value["type_name_alias"])))
    if "original_type_name" in value:
        pairs.append(
            (f"{key_prefix}OriginalTypeName", str(value["original_type_name"]))
        )
    if "publisher_id" in value:
        pairs.append((f"{key_prefix}PublisherId", str(value["publisher_id"])))
    if "supported_major_versions" in value:
        import capo_cloudformation.types.supported_major_versions

        capo_cloudformation.types.supported_major_versions.serialize_query(
            value["supported_major_versions"],
            pairs,
            f"{key_prefix}SupportedMajorVersions",
        )


def deserialize_query(el: Element) -> RequiredActivatedType:
    out: RequiredActivatedType = {}  # type: ignore[typeddict-item]
    child_type_name_alias = el.find("TypeNameAlias")
    if child_type_name_alias is not None:
        out["type_name_alias"] = str(child_type_name_alias.text or "")
    child_original_type_name = el.find("OriginalTypeName")
    if child_original_type_name is not None:
        out["original_type_name"] = str(child_original_type_name.text or "")
    child_publisher_id = el.find("PublisherId")
    if child_publisher_id is not None:
        out["publisher_id"] = str(child_publisher_id.text or "")
    child_supported_major_versions = el.find("SupportedMajorVersions")
    if child_supported_major_versions is not None:
        import capo_cloudformation.types.supported_major_versions

        out["supported_major_versions"] = (
            capo_cloudformation.types.supported_major_versions.deserialize_query(
                child_supported_major_versions
            )
        )
    return out
