"""Generated from Smithy shape ``com.amazonaws.memorydb#ReshardingStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.slot_migration


class ReshardingStatus(TypedDict, closed=True):
    slot_migration: NotRequired["capo_memorydb.types.slot_migration.SlotMigration"]
    """<p>The status of the online resharding slot migration</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReshardingStatus) -> dict:
    out: dict = {}
    if "slot_migration" in value:
        import capo_memorydb.types.slot_migration

        out["SlotMigration"] = (
            capo_memorydb.types.slot_migration.serialize_aws_json_1_1(
                value["slot_migration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReshardingStatus:
    out: ReshardingStatus = {}  # type: ignore[typeddict-item]
    if data.get("SlotMigration") is not None:
        import capo_memorydb.types.slot_migration

        out["slot_migration"] = (
            capo_memorydb.types.slot_migration.deserialize_aws_json_1_1(
                data["SlotMigration"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReshardingStatus) -> dict:
    out: dict = {}
    if "slot_migration" in value:
        import capo_memorydb.types.slot_migration

        out["SlotMigration"] = capo_memorydb.types.slot_migration.serialize_cbor(
            value["slot_migration"]
        )
    return out


def deserialize_cbor(data: dict) -> ReshardingStatus:
    out: ReshardingStatus = {}  # type: ignore[typeddict-item]
    if data.get("SlotMigration") is not None:
        import capo_memorydb.types.slot_migration

        out["slot_migration"] = capo_memorydb.types.slot_migration.deserialize_cbor(
            data["SlotMigration"]
        )
    return out
