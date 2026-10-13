"""Generated from Smithy shape ``com.amazonaws.rds#OptionSettingConfigurationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.option_setting

OptionSettingConfigurationList: TypeAlias = list[
    "capo_rds.types.option_setting.OptionSetting"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionSettingConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.option_setting

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.option_setting.serialize_query(
            item, pairs, f"{prefix}.OptionSetting.{n}"
        )


def deserialize_query(el: Element) -> OptionSettingConfigurationList:
    import capo_rds.types.option_setting

    out: OptionSettingConfigurationList = []
    for child in el.findall("OptionSetting"):
        out.append(capo_rds.types.option_setting.deserialize_query(child))
    return out


def serialize_query_flat(
    value: OptionSettingConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.option_setting

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.option_setting.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> OptionSettingConfigurationList:
    import capo_rds.types.option_setting

    out: OptionSettingConfigurationList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.option_setting.deserialize_query(child))
    return out


def redact_sensitive(value: OptionSettingConfigurationList) -> list[Any]:
    import capo_rds.types.option_setting

    return [capo_rds.types.option_setting.redact_sensitive(item) for item in value]
