"""Generated from Smithy shape ``com.amazonaws.codedeploy#OnPremisesTagSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.on_premises_tag_set_list


class OnPremisesTagSet(TypedDict, closed=True):
    on_premises_tag_set_list: NotRequired[
        "capo_codedeploy.types.on_premises_tag_set_list.OnPremisesTagSetList"
    ]
    """<p>A list that contains other lists of on-premises instance tag groups. For an instance to be included in the deployment group, it must be identified by all of the tag groups in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OnPremisesTagSet) -> dict:
    out: dict = {}
    if "on_premises_tag_set_list" in value:
        import capo_codedeploy.types.on_premises_tag_set_list

        out["onPremisesTagSetList"] = (
            capo_codedeploy.types.on_premises_tag_set_list.serialize_aws_json_1_1(
                value["on_premises_tag_set_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OnPremisesTagSet:
    out: OnPremisesTagSet = {}  # type: ignore[typeddict-item]
    if data.get("onPremisesTagSetList") is not None:
        import capo_codedeploy.types.on_premises_tag_set_list

        out["on_premises_tag_set_list"] = (
            capo_codedeploy.types.on_premises_tag_set_list.deserialize_aws_json_1_1(
                data["onPremisesTagSetList"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OnPremisesTagSet) -> dict:
    out: dict = {}
    if "on_premises_tag_set_list" in value:
        import capo_codedeploy.types.on_premises_tag_set_list

        out["onPremisesTagSetList"] = (
            capo_codedeploy.types.on_premises_tag_set_list.serialize_cbor(
                value["on_premises_tag_set_list"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> OnPremisesTagSet:
    out: OnPremisesTagSet = {}  # type: ignore[typeddict-item]
    if data.get("onPremisesTagSetList") is not None:
        import capo_codedeploy.types.on_premises_tag_set_list

        out["on_premises_tag_set_list"] = (
            capo_codedeploy.types.on_premises_tag_set_list.deserialize_cbor(
                data["onPremisesTagSetList"]
            )
        )
    return out
