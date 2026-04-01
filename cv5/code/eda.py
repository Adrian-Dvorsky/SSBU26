from data_handling import Dataset

if __name__ == "__main__":
    dataset = Dataset()

    # print statistics
    print(dataset.calculate_statistics())

    # print sumarize_feature
    print(dataset.summarize_features())

    # plot class distribution
    dataset.plot_class_distribution()

    # plot correlation matrix
    dataset.plot_correlation_matrix()

    # plot feature importance
    dataset.feature_importance()

    # plot feature distributions
    dataset.plot_feature_distributions()

    # plot box plots
    dataset.plot_box_plots()

    # plot pair plot for the first 5 features
    selected_features = dataset.feature_names[:5]
    dataset.plot_pair_plot(selected_features)