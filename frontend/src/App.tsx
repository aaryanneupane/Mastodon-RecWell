import { useEffect, useState } from 'react';
import './App.css';
import ImageViewer from './ImageViewer';

function App() {
  interface Post {
    account: {
      display_name: string;
      username: string;
      avatar: string;
      url: string;
    };
    content: string;
    media_attachments: {
      url: string;
      description: string;
    }[];
  }

  const [data, setData] = useState<Post[]>([]);
  const [selectedImage, setSelectedImage] = useState<string | null>(null);
  const [maxPages, setMaxPages] = useState(10); // Start with 10 pages

  useEffect(() => {
    fetchRecommendations();
  }, [maxPages]);

  const fetchRecommendations = () => {
    console.log("Fetching recommendations...");
    fetch(`http://127.0.0.1:5000/?max_pages=${maxPages}`)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(resdata => {
        setData(resdata); // Append new data to the existing list
        console.log("Fetched recommendations:", resdata);
      })
      .catch(error => {
        console.error("Error fetching recommendations:", error);
      });
  };

  const showMore = () => {
    // Fetch 10 more pages each time, starting from the last loaded page
    setMaxPages(maxPages + 10); // Increment by 10 each time "Show More" is clicked
  };

  const selectImage = (imageUrl: string) => setSelectedImage(imageUrl);

  return (
    <>
      <div className="max-w-2xl mx-auto py-5 px-4 text-white rounded-lg border border-gray-800 shadow-lg">
        <h1 className="text-3xl font-bold text-center mb-6 text-white">Mastodon Feed</h1>
        {data.map((post, index) => (
          <div
            key={index}
            className="post bg-gray-800 p-6 rounded-md border border-gray-700 shadow-sm mb-6 transition-all"
          >
            <div className="flex items-center mb-4">
              <img
                className="h-12 w-12 rounded-full mr-3 border border-gray-600"
                src={post.account.avatar}
                alt={post.account.display_name}
              />
              <div className="flex flex-col">
                <a
                  href={post.account.url}
                  className="text-lg font-semibold text-white hover:underline text-left"
                >
                  {post.account.display_name}
                </a>
                <h2 className="text-sm text-gray-400 text-left">@{post.account.username}</h2>
              </div>
            </div>
            <div
              className="text-gray-300 text-sm leading-relaxed space-y-4 mb-3 text-left font-medium"
              dangerouslySetInnerHTML={{ __html: post.content }}
            />
            {post.media_attachments.length > 0 && (
              <div className="media flex flex-col gap-3 mt-3">
                {post.media_attachments.map((media, mediaIndex) => (
                  <div key={mediaIndex} className="relative w-full overflow-hidden rounded-lg">
                    <img
                      src={media.url}
                      alt={media.description}
                      className="w-full h-auto object-cover hover:cursor-pointer hover:opacity-70 transition-opacity"
                      onClick={() => selectImage(media.url)}
                    />
                  </div>
                ))}
              </div>
            )}
          </div>
        ))}
        <button
          className="bg-blue-500 text-white px-4 py-2 rounded-lg mt-6 hover:bg-blue-600 transition-colors font-semibold"
          onClick={showMore}
        >
          Show More
        </button>
        {selectedImage && (
          <ImageViewer imageUrl={selectedImage} onClose={() => setSelectedImage(null)} />
        )}
      </div>
    </>
  );
}

export default App;
