"""Generated from Smithy shape ``com.amazonaws.autoscaling#PutAccountSettingAnswer``."""

from typing_extensions import TypedDict

from capo_auto_scaling._protocol.xml import Element


class PutAccountSettingAnswer(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: PutAccountSettingAnswer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> PutAccountSettingAnswer:
    out: PutAccountSettingAnswer = {}  # type: ignore[typeddict-item]
    return out
