import axios from 'axios';
import { useQuery } from 'react-query';

const fetchJobData = async () => {
    const response = await axios.get('/api/jobs');
    return response.data;
};

export default function useJobData() {
    return useQuery('job-data', fetchJobData, {
        staleTime: 1000,
        cacheTime: 30000
    });
}
