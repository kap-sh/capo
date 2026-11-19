"""Generated from Smithy shape ``com.amazonaws.translate#GetParallelDataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.parallel_data_data_location
    import capo_translate.types.parallel_data_properties


class GetParallelDataResponse(TypedDict, closed=True):
    parallel_data_properties: NotRequired[
        "capo_translate.types.parallel_data_properties.ParallelDataProperties"
    ]
    """<p>The properties of the parallel data resource that is being retrieved.</p>"""
    data_location: NotRequired[
        "capo_translate.types.parallel_data_data_location.ParallelDataDataLocation"
    ]
    """<p>The Amazon S3 location of the most recent parallel data input file that was successfully imported into Amazon Translate. The location is returned as a presigned URL that has a 30-minute expiration.</p> <important> <p>Amazon Translate doesn't scan all input files for the risk of CSV injection attacks. </p> <p>CSV injection occurs when a .csv or .tsv file is altered so that a record contains malicious code. The record begins with a special character, such as =, +, -, or @. When the file is opened in a spreadsheet program, the program might interpret the record as a formula and run the code within it.</p> <p>Before you download an input file from Amazon S3, ensure that you recognize the file and trust its creator.</p> </important>"""
    auxiliary_data_location: NotRequired[
        "capo_translate.types.parallel_data_data_location.ParallelDataDataLocation"
    ]
    """<p>The Amazon S3 location of a file that provides any errors or warnings that were produced by your input file. This file was created when Amazon Translate attempted to create a parallel data resource. The location is returned as a presigned URL to that has a 30-minute expiration.</p>"""
    latest_update_attempt_auxiliary_data_location: NotRequired[
        "capo_translate.types.parallel_data_data_location.ParallelDataDataLocation"
    ]
    """<p>The Amazon S3 location of a file that provides any errors or warnings that were produced by your input file. This file was created when Amazon Translate attempted to update a parallel data resource. The location is returned as a presigned URL to that has a 30-minute expiration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetParallelDataResponse) -> dict:
    out: dict = {}
    if "parallel_data_properties" in value:
        import capo_translate.types.parallel_data_properties

        out["ParallelDataProperties"] = (
            capo_translate.types.parallel_data_properties.serialize_aws_json_1_1(
                value["parallel_data_properties"]
            )
        )
    if "data_location" in value:
        import capo_translate.types.parallel_data_data_location

        out["DataLocation"] = (
            capo_translate.types.parallel_data_data_location.serialize_aws_json_1_1(
                value["data_location"]
            )
        )
    if "auxiliary_data_location" in value:
        import capo_translate.types.parallel_data_data_location

        out["AuxiliaryDataLocation"] = (
            capo_translate.types.parallel_data_data_location.serialize_aws_json_1_1(
                value["auxiliary_data_location"]
            )
        )
    if "latest_update_attempt_auxiliary_data_location" in value:
        import capo_translate.types.parallel_data_data_location

        out["LatestUpdateAttemptAuxiliaryDataLocation"] = (
            capo_translate.types.parallel_data_data_location.serialize_aws_json_1_1(
                value["latest_update_attempt_auxiliary_data_location"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetParallelDataResponse:
    out: GetParallelDataResponse = {}  # type: ignore[typeddict-item]
    if data.get("ParallelDataProperties") is not None:
        import capo_translate.types.parallel_data_properties

        out["parallel_data_properties"] = (
            capo_translate.types.parallel_data_properties.deserialize_aws_json_1_1(
                data["ParallelDataProperties"]
            )
        )
    if data.get("DataLocation") is not None:
        import capo_translate.types.parallel_data_data_location

        out["data_location"] = (
            capo_translate.types.parallel_data_data_location.deserialize_aws_json_1_1(
                data["DataLocation"]
            )
        )
    if data.get("AuxiliaryDataLocation") is not None:
        import capo_translate.types.parallel_data_data_location

        out["auxiliary_data_location"] = (
            capo_translate.types.parallel_data_data_location.deserialize_aws_json_1_1(
                data["AuxiliaryDataLocation"]
            )
        )
    if data.get("LatestUpdateAttemptAuxiliaryDataLocation") is not None:
        import capo_translate.types.parallel_data_data_location

        out["latest_update_attempt_auxiliary_data_location"] = (
            capo_translate.types.parallel_data_data_location.deserialize_aws_json_1_1(
                data["LatestUpdateAttemptAuxiliaryDataLocation"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetParallelDataResponse) -> dict:
    out: dict = {}
    if "parallel_data_properties" in value:
        import capo_translate.types.parallel_data_properties

        out["ParallelDataProperties"] = (
            capo_translate.types.parallel_data_properties.serialize_cbor(
                value["parallel_data_properties"]
            )
        )
    if "data_location" in value:
        import capo_translate.types.parallel_data_data_location

        out["DataLocation"] = (
            capo_translate.types.parallel_data_data_location.serialize_cbor(
                value["data_location"]
            )
        )
    if "auxiliary_data_location" in value:
        import capo_translate.types.parallel_data_data_location

        out["AuxiliaryDataLocation"] = (
            capo_translate.types.parallel_data_data_location.serialize_cbor(
                value["auxiliary_data_location"]
            )
        )
    if "latest_update_attempt_auxiliary_data_location" in value:
        import capo_translate.types.parallel_data_data_location

        out["LatestUpdateAttemptAuxiliaryDataLocation"] = (
            capo_translate.types.parallel_data_data_location.serialize_cbor(
                value["latest_update_attempt_auxiliary_data_location"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetParallelDataResponse:
    out: GetParallelDataResponse = {}  # type: ignore[typeddict-item]
    if data.get("ParallelDataProperties") is not None:
        import capo_translate.types.parallel_data_properties

        out["parallel_data_properties"] = (
            capo_translate.types.parallel_data_properties.deserialize_cbor(
                data["ParallelDataProperties"]
            )
        )
    if data.get("DataLocation") is not None:
        import capo_translate.types.parallel_data_data_location

        out["data_location"] = (
            capo_translate.types.parallel_data_data_location.deserialize_cbor(
                data["DataLocation"]
            )
        )
    if data.get("AuxiliaryDataLocation") is not None:
        import capo_translate.types.parallel_data_data_location

        out["auxiliary_data_location"] = (
            capo_translate.types.parallel_data_data_location.deserialize_cbor(
                data["AuxiliaryDataLocation"]
            )
        )
    if data.get("LatestUpdateAttemptAuxiliaryDataLocation") is not None:
        import capo_translate.types.parallel_data_data_location

        out["latest_update_attempt_auxiliary_data_location"] = (
            capo_translate.types.parallel_data_data_location.deserialize_cbor(
                data["LatestUpdateAttemptAuxiliaryDataLocation"]
            )
        )
    return out
