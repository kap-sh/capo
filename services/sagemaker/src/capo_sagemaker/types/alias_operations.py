"""Generated from Smithy shape ``com.amazonaws.sagemaker#AliasOperations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.pipeline_version_alias_list


class AliasOperations(TypedDict, closed=True):
    add: NotRequired[
        "capo_sagemaker.types.pipeline_version_alias_list.PipelineVersionAliasList"
    ]
    """<p>The aliases to add to the pipeline version. If you assigned an alias to another version of the same pipeline, you must remove it from that version before you add it here.</p>"""
    remove: NotRequired[
        "capo_sagemaker.types.pipeline_version_alias_list.PipelineVersionAliasList"
    ]
    """<p>The aliases to remove from the pipeline version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AliasOperations) -> dict:
    out: dict = {}
    if "add" in value:
        import capo_sagemaker.types.pipeline_version_alias_list

        out["Add"] = (
            capo_sagemaker.types.pipeline_version_alias_list.serialize_aws_json_1_1(
                value["add"]
            )
        )
    if "remove" in value:
        import capo_sagemaker.types.pipeline_version_alias_list

        out["Remove"] = (
            capo_sagemaker.types.pipeline_version_alias_list.serialize_aws_json_1_1(
                value["remove"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AliasOperations:
    out: AliasOperations = {}  # type: ignore[typeddict-item]
    if data.get("Add") is not None:
        import capo_sagemaker.types.pipeline_version_alias_list

        out["add"] = (
            capo_sagemaker.types.pipeline_version_alias_list.deserialize_aws_json_1_1(
                data["Add"]
            )
        )
    if data.get("Remove") is not None:
        import capo_sagemaker.types.pipeline_version_alias_list

        out["remove"] = (
            capo_sagemaker.types.pipeline_version_alias_list.deserialize_aws_json_1_1(
                data["Remove"]
            )
        )
    return out
