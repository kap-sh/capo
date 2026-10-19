"""Generated from Smithy shape ``com.amazonaws.codecommit#PutRepositoryTriggersInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.repository_name
    import capo_codecommit.types.repository_triggers_list


class PutRepositoryTriggersInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository where you want to create or update the trigger.</p>"""
    triggers: "capo_codecommit.types.repository_triggers_list.RepositoryTriggersList"
    """<p>The JSON block of configuration information for each trigger.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRepositoryTriggersInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    import capo_codecommit.types.repository_triggers_list

    out["triggers"] = (
        capo_codecommit.types.repository_triggers_list.serialize_aws_json_1_1(
            value["triggers"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRepositoryTriggersInput:
    out: PutRepositoryTriggersInput = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("triggers") is not None:
        import capo_codecommit.types.repository_triggers_list

        out["triggers"] = (
            capo_codecommit.types.repository_triggers_list.deserialize_aws_json_1_1(
                data["triggers"]
            )
        )
    else:
        out["triggers"] = []
    return out
