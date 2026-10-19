"""Generated from Smithy shape ``com.amazonaws.codecommit#TestRepositoryTriggersInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.repository_name
    import capo_codecommit.types.repository_triggers_list


class TestRepositoryTriggersInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository in which to test the triggers.</p>"""
    triggers: "capo_codecommit.types.repository_triggers_list.RepositoryTriggersList"
    """<p>The list of triggers to test.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestRepositoryTriggersInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    import capo_codecommit.types.repository_triggers_list

    out["triggers"] = (
        capo_codecommit.types.repository_triggers_list.serialize_aws_json_1_1(
            value["triggers"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TestRepositoryTriggersInput:
    out: TestRepositoryTriggersInput = {}  # type: ignore[typeddict-item]
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
