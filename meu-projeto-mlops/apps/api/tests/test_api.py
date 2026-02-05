from meu.common.logger import log

from api.main import func_main


def test_func_main_integration() -> None:

    input_msg = "MLOps é Vida"

    log()

    result = func_main(input_msg)

    assert result == input_msg
