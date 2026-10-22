"""Generated from Smithy shape ``com.amazonaws.autoscaling#AccountSettings``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.account_setting

AccountSettings: TypeAlias = list[
    "capo_auto_scaling.types.account_setting.AccountSetting"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AccountSettings, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.account_setting

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.account_setting.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AccountSettings:
    import capo_auto_scaling.types.account_setting

    out: AccountSettings = []
    for child in el.findall("member"):
        out.append(capo_auto_scaling.types.account_setting.deserialize_query(child))
    return out


def serialize_query_flat(
    value: AccountSettings, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.account_setting

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.account_setting.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AccountSettings:
    import capo_auto_scaling.types.account_setting

    out: AccountSettings = []
    for child in parent.findall(tag):
        out.append(capo_auto_scaling.types.account_setting.deserialize_query(child))
    return out
