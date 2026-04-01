from data_handling import Dataset

if __name__ == "__main__":
    dataset = Dataset()

    # print statistics
    print(dataset.calculate_statistics())

    # print sumarize_feature
    print(dataset.summarize_features())
    print(dataset.summarize_features(["worst fractal dimension"]))

    x_std, _ = dataset.scale_data(dataset.data,dataset.data,scale_type='standard')
    x_norm, _ = dataset.scale_data(dataset.data,dataset.data,scale_type='normalize')
    x_robust, _ = dataset.scale_data(dataset.data,dataset.data,scale_type='robust')

    feature = "worst fractal dimension"

    # standardization

    dataset.plot_all_features_before_after_scaling(dataset.data, x_std, 'standard')
    dataset.plot_feature_before_after_scaling(dataset.data, x_std, feature)
    dataset.plot_box_plots(x_std)

    # normalize

    dataset.plot_all_features_before_after_scaling(dataset.data, x_norm, 'normalize')
    dataset.plot_feature_before_after_scaling(dataset.data, x_norm, feature)
    dataset.plot_box_plots(x_norm)

    # robust

    dataset.plot_all_features_before_after_scaling(dataset.data, x_robust, 'robust')
    dataset.plot_feature_before_after_scaling(dataset.data, x_robust, feature)
    dataset.plot_box_plots(x_robust)


    #dataset.plot_feature_before_after_scaling(dataset.data,x_std, feature)
    #dataset.plot_feature_before_after_scaling(dataset.data, x_norm, feature)
    #dataset.plot_feature_before_after_scaling(dataset.data, x_robust, feature)
