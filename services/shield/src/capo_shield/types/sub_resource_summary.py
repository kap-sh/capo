"""Generated from Smithy shape ``com.amazonaws.shield#SubResourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.string
    import capo_shield.types.sub_resource_type
    import capo_shield.types.summarized_attack_vector_list
    import capo_shield.types.summarized_counter_list


class SubResourceSummary(TypedDict, closed=True):
    type: NotRequired["capo_shield.types.sub_resource_type.SubResourceType"]
    """<p>The <code>SubResource</code> type.</p>"""
    id: NotRequired["capo_shield.types.string.String"]
    """<p>The unique identifier (ID) of the <code>SubResource</code>.</p>"""
    attack_vectors: NotRequired[
        "capo_shield.types.summarized_attack_vector_list.SummarizedAttackVectorList"
    ]
    """<p>The list of attack types and associated counters.</p>"""
    counters: NotRequired[
        "capo_shield.types.summarized_counter_list.SummarizedCounterList"
    ]
    """<p>The counters that describe the details of the attack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubResourceSummary) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_shield.types.sub_resource_type

        out["Type"] = capo_shield.types.sub_resource_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "attack_vectors" in value:
        import capo_shield.types.summarized_attack_vector_list

        out["AttackVectors"] = (
            capo_shield.types.summarized_attack_vector_list.serialize_aws_json_1_1(
                value["attack_vectors"]
            )
        )
    if "counters" in value:
        import capo_shield.types.summarized_counter_list

        out["Counters"] = (
            capo_shield.types.summarized_counter_list.serialize_aws_json_1_1(
                value["counters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SubResourceSummary:
    out: SubResourceSummary = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_shield.types.sub_resource_type

        out["type"] = capo_shield.types.sub_resource_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("AttackVectors") is not None:
        import capo_shield.types.summarized_attack_vector_list

        out["attack_vectors"] = (
            capo_shield.types.summarized_attack_vector_list.deserialize_aws_json_1_1(
                data["AttackVectors"]
            )
        )
    if data.get("Counters") is not None:
        import capo_shield.types.summarized_counter_list

        out["counters"] = (
            capo_shield.types.summarized_counter_list.deserialize_aws_json_1_1(
                data["Counters"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SubResourceSummary) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_shield.types.sub_resource_type

        out["Type"] = capo_shield.types.sub_resource_type.serialize_cbor(value["type"])
    if "id" in value:
        out["Id"] = value["id"]
    if "attack_vectors" in value:
        import capo_shield.types.summarized_attack_vector_list

        out["AttackVectors"] = (
            capo_shield.types.summarized_attack_vector_list.serialize_cbor(
                value["attack_vectors"]
            )
        )
    if "counters" in value:
        import capo_shield.types.summarized_counter_list

        out["Counters"] = capo_shield.types.summarized_counter_list.serialize_cbor(
            value["counters"]
        )
    return out


def deserialize_cbor(data: dict) -> SubResourceSummary:
    out: SubResourceSummary = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_shield.types.sub_resource_type

        out["type"] = capo_shield.types.sub_resource_type.deserialize_cbor(data["Type"])
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("AttackVectors") is not None:
        import capo_shield.types.summarized_attack_vector_list

        out["attack_vectors"] = (
            capo_shield.types.summarized_attack_vector_list.deserialize_cbor(
                data["AttackVectors"]
            )
        )
    if data.get("Counters") is not None:
        import capo_shield.types.summarized_counter_list

        out["counters"] = capo_shield.types.summarized_counter_list.deserialize_cbor(
            data["Counters"]
        )
    return out
