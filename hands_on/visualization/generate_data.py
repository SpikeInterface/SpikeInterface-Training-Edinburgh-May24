import spikeinterface.full as si

from pathlib import Path

base_folder = Path('/home/samuel/DataSpikeSorting/Edinburgh_SI_tutos/')

si.set_global_job_kwargs(n_jobs=-1, progress_bar=True, chunk_duration="1s")


def gen_data():
    static_recording, drifting_recording, gt_sorting = si.generate_drifting_recording(
        num_units=50,
        duration=150.,
        probe_name="Neuronexus-32",
        # probe_name="Neuropixel-128",

        generate_templates_kwargs=dict(
            ms_before=1.5,
            ms_after=3.0,
            mode="ellipsoid",
            unit_params=dict(
                alpha=(150.0, 500.0),
                spatial_decay=(10, 40),
            ),
        ),
        generate_unit_locations_kwargs=dict(
            margin_um=10.0,
            minimum_z=6.0,
            maximum_z=25.0,
            minimum_distance=18.0,
            max_iteration=100,
            distance_strict=False,
        ),    
        generate_sorting_kwargs=dict(
            firing_rates=(2.0, 5.0),
            refractory_period_ms=4.0
        ),
        generate_noise_kwargs=dict(
            noise_levels=(12.0, 15.0),
            spatial_decay=25.0
        ),
        generate_displacement_vector_kwargs=dict(
            displacement_sampling_frequency=5.0,
            drift_start_um=[0, 6],
            drift_stop_um=[0, -5],
            drift_step_um=1,
            motion_list=[
                dict(
                    drift_mode="zigzag",
                    non_rigid_gradient=None,
                    t_start_drift=0.0,
                    t_end_drift=None,
                    period_s=300.,
                ),
            ],
        ),

        seed=2205
    )

    gt_analyzer = si.create_sorting_analyzer(gt_sorting, drifting_recording, sparse=True)
    gt_analyzer.compute(["random_spikes", "waveforms", "templates", "noise_levels"])
    gt_analyzer.compute(["spike_amplitudes", "unit_locations",  "correlograms", "template_similarity"])
    # "principal_components",
    gt_analyzer.compute("quality_metrics", metric_names=["snr", "amplitude_cutoff", "rp_violation"])
    gt_analyzer

    si.plot_sorting_summary(gt_analyzer, backend="spikeinterface_gui")


    drifting_recording.save(folder=base_folder / "postprocessing_data" /  "recording")
    gt_sorting.save(folder=base_folder / "postprocessing_data" /  "gt_sorting")



def run():
    rec = si.load_extractor(base_folder / "postprocessing_data" /  "recording")
    sorting_sc2 = si.run_sorter("spykingcircus2", rec,
                                output_folder=base_folder / "postprocessing_data" / "sorter_SC2",
                                verbose=True,
                                )

    sorting = sorting_sc2.save(folder=base_folder / "postprocessing_data" / "sorting_mysterious")
    print(sorting_sc2)
    print(sorting)

def sc2_analyzer():
    rec = si.load_extractor(base_folder / "postprocessing_data" /  "recording")
    sorting = si.load_extractor(base_folder /  "postprocessing_data" / "sorting_mysterious")
    print(sorting)   

    gt_analyzer = si.create_sorting_analyzer(sorting, rec, sparse=True)
    gt_analyzer.compute(["random_spikes", "waveforms", "templates", "noise_levels"])
    gt_analyzer.compute(["spike_amplitudes", "unit_locations",  "correlograms", "template_similarity"])
    # "principal_components",
    gt_analyzer.compute("quality_metrics", metric_names=["snr", "amplitude_cutoff", "rp_violation"])
    gt_analyzer

    gt_analyzer.save_as(folder=base_folder / "SC2_analyzer", format="binary_folder")

    si.plot_sorting_summary(gt_analyzer, backend="spikeinterface_gui")


if __name__ == "__main__":

    # gen_data()
    # run()
    sc2_analyzer()


