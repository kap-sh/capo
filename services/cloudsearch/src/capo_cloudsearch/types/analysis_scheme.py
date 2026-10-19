"""Generated from Smithy shape ``com.amazonaws.cloudsearch#AnalysisScheme``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.analysis_options
    import capo_cloudsearch.types.analysis_scheme_language
    import capo_cloudsearch.types.standard_name


class AnalysisScheme(TypedDict, closed=True):
    analysis_scheme_name: "capo_cloudsearch.types.standard_name.StandardName"
    analysis_scheme_language: (
        "capo_cloudsearch.types.analysis_scheme_language.AnalysisSchemeLanguage"
    )
    analysis_options: NotRequired[
        "capo_cloudsearch.types.analysis_options.AnalysisOptions"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: AnalysisScheme, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (f"{key_prefix}AnalysisSchemeName", str(value["analysis_scheme_name"]))
    )
    import capo_cloudsearch.types.analysis_scheme_language

    capo_cloudsearch.types.analysis_scheme_language.serialize_query(
        value["analysis_scheme_language"], pairs, f"{key_prefix}AnalysisSchemeLanguage"
    )
    if "analysis_options" in value:
        import capo_cloudsearch.types.analysis_options

        capo_cloudsearch.types.analysis_options.serialize_query(
            value["analysis_options"], pairs, f"{key_prefix}AnalysisOptions"
        )


def deserialize_query(el: Element) -> AnalysisScheme:
    out: AnalysisScheme = {}  # type: ignore[typeddict-item]
    child_analysis_scheme_name = el.find("AnalysisSchemeName")
    if child_analysis_scheme_name is not None:
        out["analysis_scheme_name"] = str(child_analysis_scheme_name.text or "")
    else:
        out["analysis_scheme_name"] = ""
    child_analysis_scheme_language = el.find("AnalysisSchemeLanguage")
    if child_analysis_scheme_language is not None:
        import capo_cloudsearch.types.analysis_scheme_language

        out["analysis_scheme_language"] = (
            capo_cloudsearch.types.analysis_scheme_language.deserialize_query(
                child_analysis_scheme_language
            )
        )
    else:
        import typing

        out["analysis_scheme_language"] = typing.cast(
            "capo_cloudsearch.types.analysis_scheme_language.AnalysisSchemeLanguage", ""
        )
    child_analysis_options = el.find("AnalysisOptions")
    if child_analysis_options is not None:
        import capo_cloudsearch.types.analysis_options

        out["analysis_options"] = (
            capo_cloudsearch.types.analysis_options.deserialize_query(
                child_analysis_options
            )
        )
    return out
