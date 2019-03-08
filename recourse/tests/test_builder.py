from recourse.tests.fixtures import *


def test_rb_basic(data, recourse_builder):
    print(recourse_builder)


def test_rb_fit_without_initialization(data, recourse_builder):
    """Test fitting on a denied individual, CPLEX."""

    # pick a denied individual
    try:
        output = recourse_builder.fit()
    except AssertionError:
        assert True
    else:
        assert False


def test_rb_fit(data, recourse_builder, features):
    print(len(features))
    print(recourse_builder.n_variables)
    recourse_builder.x = features
    output = recourse_builder.fit()
    output['cost'] >= 0.0








