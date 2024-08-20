import axios from 'axios';

export default async function handler(req, res) {
    if (req.method === 'POST') {
        const jobData = await axios.post('/api/jobs', req.body);
        return res.status(201).json(jobData.data);
    } else if (req.method === 'GET') {
        const jobData = await axios.get('/api/jobs');
        return res.status(200).json(jobData.data);
    }
}
