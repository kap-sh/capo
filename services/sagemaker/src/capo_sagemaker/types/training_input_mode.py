"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingInputMode``."""

from typing import Literal, TypeAlias, cast

"""<p>The training input mode that the algorithm supports. For more information about input modes, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html">Algorithms</a>.</p> <p> <b>Pipe mode</b> </p> <p>If an algorithm supports <code>Pipe</code> mode, Amazon SageMaker streams data directly from Amazon S3 to the container.</p> <p> <b>File mode</b> </p> <p>If an algorithm supports <code>File</code> mode, SageMaker downloads the training data from S3 to the provisioned ML storage volume, and mounts the directory to the Docker volume for the training container.</p> <p>You must provision the ML storage volume with sufficient capacity to accommodate the data downloaded from S3. In addition to the training data, the ML storage volume also stores the output model. The algorithm container uses the ML storage volume to also store intermediate information, if any.</p> <p>For distributed algorithms, training data is distributed uniformly. Your training duration is predictable if the input data objects sizes are approximately the same. SageMaker does not split the files any further for model training. If the object sizes are skewed, training won't be optimal as the data distribution is also skewed when one host in a training cluster is overloaded, thus becoming a bottleneck in training.</p> <p> <b>FastFile mode</b> </p> <p>If an algorithm supports <code>FastFile</code> mode, SageMaker streams data directly from S3 to the container with no code changes, and provides file system access to the data. Users can author their training script to interact with these files as if they were stored on disk.</p> <p> <code>FastFile</code> mode works best when the data is read sequentially. Augmented manifest files aren't supported. The startup time is lower when there are fewer files in the S3 bucket provided.</p>"""
TrainingInputMode: TypeAlias = Literal[
    "Pipe",
    "File",
    "FastFile",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingInputMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingInputMode:
    return cast(TrainingInputMode, data)
