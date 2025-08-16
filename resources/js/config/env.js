const origin = typeof window !== 'undefined' ? window.location.origin : '';
const ENV = {
    API_URL: process.env.MIX_HOST || origin,
    DEMO: process.env.MIX_DEMO || false,
    API_KEY: process.env.MIX_API_KEY || ''
};
export default ENV;