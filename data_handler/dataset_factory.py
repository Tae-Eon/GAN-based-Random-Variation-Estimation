import data_handler.dataset as data

class DatasetFactory:
    def __init__(self):
        pass
    
    def get_dataset(args):
        if args.trainer == 'mlp_gaussian':
            
            # LER
            if args.dataset == '2020_LER_20201008_V008.xlsx':
                return data.SEMI_gaussian_data(args.dataset, one_hot=args.one_hot, num_of_input=args.num_of_input, num_in_cycle=args.tr_num_in_cycle, num_of_cycle=127, num_train=127, num_val=0)

            # RDF, WFV, RDF+WFV
            elif args.dataset == 'rdfwfv_wfv_rdf_train2020_RDFWFV_20201222_V10.xlsx' or args.dataset == 'updated_rdfwfv_wfv_rdf_train2020_RDFWFV_20201222_V10.xlsx':
                return data.SEMI_gaussian_data(args.dataset, one_hot=args.one_hot, num_of_input=args.num_of_input, num_in_cycle=args.tr_num_in_cycle, num_of_cycle=200, num_train=200, num_val=0)
            
            # LER&RDF&WFV
            elif args.dataset == 'train_LERRDFWFV_167set+Testdataset_4set_V002.xlsx':
                return data.SEMI_gaussian_data(args.dataset, one_hot=args.one_hot, num_of_input=args.num_of_input, num_in_cycle=args.tr_num_in_cycle, num_of_cycle=167, num_train=167, num_val=0)
            elif args.dataset == 'updated_train_LERRDFWFV_167set+Testdataset_4set_V002.xlsx':
                return data.SEMI_gaussian_data(args.dataset, one_hot=args.one_hot, num_of_input=args.num_of_input, num_in_cycle=args.tr_num_in_cycle, num_of_cycle=159, num_train=159, num_val=0)


        elif args.trainer == 'gan' or 'wgan':
            # LER

            if args.dataset == '2020_LER_20201008_V008.xlsx':
                return data.SEMI_gan_data(args.dataset, one_hot=args.one_hot, num_of_input=args.num_of_input, num_in_cycle=args.tr_num_in_cycle, num_of_cycle=127, num_train=127, num_val=0)
            
            # RDF, WFV, RDF+WFV
            
            elif args.dataset == 'rdfwfv_wfv_rdf_train2020_RDFWFV_20201222_V10.xlsx' or args.dataset == 'updated_rdfwfv_wfv_rdf_train2020_RDFWFV_20201222_V10.xlsx':
                return data.SEMI_gan_data(args.dataset, one_hot=args.one_hot, num_of_input=args.num_of_input, num_in_cycle=args.tr_num_in_cycle, num_of_cycle=200, num_train=200, num_val=0)
            
            elif args.dataset == 'train_LERRDFWFV_167set+Testdataset_4set_V002.xlsx':
                return data.SEMI_gan_data(args.dataset, one_hot=args.one_hot, num_of_input=args.num_of_input, num_in_cycle=args.tr_num_in_cycle, num_of_cycle=167, num_train=167, num_val=0)
            elif args.dataset == 'updated_train_LERRDFWFV_167set+Testdataset_4set_V002.xlsx':
                return data.SEMI_gan_data(args.dataset, one_hot=args.one_hot, num_of_input=args.num_of_input, num_in_cycle=args.tr_num_in_cycle, num_of_cycle=159, num_train=159, num_val=0) 

        
    def get_test_dataset(args):

        if args.dataset_test == '2020_LER_20201102_testset_V04.xlsx' or args.dataset_test == 'rdfwfv_wfv_rdf_train2020_RDFWFV_20201222_V10.xlsx' or args.dataset_test == '2021_RDFWFV_20210107.xlsx' or args.dataset_test == 'test_LERRDFWFV_167set+Testdataset_4set_V002.xlsx' or args.dataset_test == 'updated_test_LERRDFWFV_167set+Testdataset_4set_V002.xlsx' or args.dataset_test == 'updated_2021_RDFWFV_20210107.xlsx':
            return data.SEMI_sample_data(args.dataset_test)
